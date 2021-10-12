import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-rio-grande-do-norte',
  templateUrl: './rio-grande-do-norte.component.html',
  styleUrls: ['./rio-grande-do-norte.component.css']
})
export class RioGrandeDoNorteComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
