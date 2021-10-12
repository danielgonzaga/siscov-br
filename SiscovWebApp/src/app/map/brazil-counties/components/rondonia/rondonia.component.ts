import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-rondonia',
  templateUrl: './rondonia.component.html',
  styleUrls: ['./rondonia.component.css']
})
export class RondoniaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
