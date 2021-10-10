import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParaibaComponent } from './paraiba.component';

describe('ParaibaComponent', () => {
  let component: ParaibaComponent;
  let fixture: ComponentFixture<ParaibaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ParaibaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ParaibaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
