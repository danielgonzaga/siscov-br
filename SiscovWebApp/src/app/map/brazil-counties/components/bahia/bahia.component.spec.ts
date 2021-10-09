import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BahiaComponent } from './bahia.component';

describe('BahiaComponent', () => {
  let component: BahiaComponent;
  let fixture: ComponentFixture<BahiaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BahiaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BahiaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
